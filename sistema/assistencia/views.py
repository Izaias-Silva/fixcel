import hashlib
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Cliente, Aparelho, Agendamento, criptografar
from .forms import ClienteForm, AparelhoForm, AgendamentoForm, DataForm
 
 
# ---------------- LOGIN, SAIR E TELA PRINCIPAL ----------------
def entrar(request):
    erro = ""
    if request.method == "POST":
        login = request.POST["login"]
        senha = request.POST["senha"]
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()
        usuario = Usuario.objects.filter(login=login, senha=senha_hash).first()
        if usuario:
            request.session["usuario_nome"] = usuario.nome
            return redirect("principal")
        erro = "Usuário ou senha inválidos."
    return render(request, "login.html", {"erro": erro})
 
 
def sair(request):
    request.session.flush()
    return redirect("login")
 
 
def principal(request):
    if "usuario_nome" not in request.session:
        return redirect("login")
    return render(request, "principal.html")


# ---------------- CLIENTES ----------------
def clientes(request):
    if "usuario_nome" not in request.session:
        return redirect("login")
    busca = request.GET.get("busca", "")
    lista = Cliente.objects.filter(nome__icontains=busca).order_by("nome")
    return render(request, "clientes.html", {"clientes": lista, "busca": busca})
 
 
def cliente_novo(request):
    if "usuario_nome" not in request.session:
        return redirect("login")
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        cliente = form.save(commit=False)
        cliente.cpf = criptografar(cliente.cpf)
        cliente.save()
        return redirect("clientes")
    return render(request, "form.html", {"form": form, "titulo": "Novo cliente"})
 
 
def cliente_editar(request, id):
    if "usuario_nome" not in request.session:
        return redirect("login")
    cliente = get_object_or_404(Cliente, id_cliente=id)
    cliente.cpf = cliente.cpf_aberto()
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        cliente = form.save(commit=False)
        cliente.cpf = criptografar(cliente.cpf)
        cliente.save()
        return redirect("clientes")
    return render(request, "form.html", {"form": form, "titulo": "Editar cliente"})

# ---------------- APARELHOS ----------------
def aparelhos(request):
    if "usuario_nome" not in request.session:
        return redirect("login")
    lista = Aparelho.objects.order_by("imei")
    return render(request, "aparelhos.html", {"aparelhos": lista})
 
 
def aparelho_novo(request):
    if "usuario_nome" not in request.session:
        return redirect("login")
    form = AparelhoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("aparelhos")
    return render(request, "form.html", {"form": form, "titulo": "Novo aparelho"})

# ---------------- AGENDAMENTOS ----------------
def agendamentos(request):
    if "usuario_nome" not in request.session:
        return redirect("login")
    lista = Agendamento.objects.order_by("data", "horario")
    return render(request, "agendamentos.html", {"agendamentos": lista})
 
 
def agendamento_novo(request):
    if "usuario_nome" not in request.session:
        return redirect("login")
    form = AgendamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("agendamentos")
    return render(request, "form.html", {"form": form, "titulo": "Novo agendamento"})
 
 
def agendamento_data(request, id):
    if "usuario_nome" not in request.session:
        return redirect("login")
    agendamento = get_object_or_404(Agendamento, id_agendamento=id)
    form = DataForm(request.POST or None, instance=agendamento)
    if form.is_valid():
        form.save()
        return redirect("agendamentos")
    return render(request, "form.html", {"form": form, "titulo": "Alterar data do agendamento"})
Ask AI
