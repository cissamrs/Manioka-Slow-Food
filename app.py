from flask import Flask, render_template
app = Flask(__name__)

produtos = [
  {
    "titulo": Geleias Artesanais",
    "descricao": " Feitas com frutas orgânicas selecionadas, sem conservantes artificiais",
    "id_caixa": "geleias"
  },
  "titulo": "Chás Fermentados", 
        "descricao": "Kombuchá e outros fermentados naturais ricos em probióticos.",
        "id_caixa": "chas"
    },
    {
        "titulo": "Pães de Fermentação Natural", 
        "descricao": "Pães artesanais com massa madre, processo tradicional de 24h.",
        "id_caixa": "paes"
    },
    {
        "titulo": "Biscoitos Integrais", 
        "descricao": "Receitas familiares com ingredientes orgânicos e integrais.",
        "id_caixa": "biscoitos"
    },
    {
        "titulo": "Doces Naturais", 
        "descricao": "Sobremesas saudáveis adoçadas com mel e frutas.",
        "id_caixa": "doces"
    },
    {
        "titulo": "Bebidas Naturais", 
        "descricao": "Sucos, águas aromatizadas e bebidas funcionais.",
        "id_caixa": "bebidas"
    }
]

@app.route('/')
def home():
    return render_templates('index.html', lisya_produtos=produtos)
if __name__ == '__main__':
    app.run(debug=True)  

# 1. Rota 
@app.route('/')
def home():
    return render_template('index.html', lista_produtos=produtos)

# 2. Nova Rota: '/sobre' 
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# 3. Nova Rota: '/contato' 
@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)