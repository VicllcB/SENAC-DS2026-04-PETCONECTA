from flask import Flask, render_template_string, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_flash_messages'

# HTML integrado para simplificar o exemplo (Templates)
LOGIN_HTML = '''
<h2>Login do Sistema</h2>
<form method="post">
    Usuário: <input type="text" name="usuario"><br><br>
    Senha: <input type="password" name="senha"><br><br>
    <button type="submit">Entrar</button>
</form>
{% with messages = get_flashed_messages() %}
  {% if messages %}<p style="color:red">{{ messages[0] }}</p>{% endif %}
{% endwith %}
'''

CADASTRO_HTML = '''
<h2>Cadastro de Produto</h2>
<form method="post">
    Produto: <input type="text" name="nome" required><br><br>
    Preço: <input type="number" step="0.01" name="preco" required><br><br>
    Qtd: <input type="number" name="qtd" required><br><br>
    <button type="submit">Cadastrar</button>
</form>
<a href="/">Sair</a>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('usuario')
        senha = request.form.get('senha')
        if user == 'admin' and senha == '1234':
            return redirect(url_for('cadastro'))
        else:
            flash('Usuário ou senha inválidos!')
    return render_template_string(LOGIN_HTML)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        # Aqui simularíamos a gravação no banco de dados
        return f"<h1>Sucesso!</h1><p>O produto {nome} foi cadastrado.</p><a href='/cadastro'>Voltar</a>"
    return render_template_string(CADASTRO_HTML)

if __name__ == '__main__':
    app.run(debug=True)
