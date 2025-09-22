# Ajustador de Códigos

Um aplicativo web Flask para ajustar códigos de planilhas, convertendo-os para o formato de 5 dígitos com zeros à esquerda e removendo letras.

## Funcionalidades

- ✨ **Ajuste automático**: Converte códigos para 5 dígitos
- 🔤 **Remove letras**: Elimina caracteres alfabéticos dos códigos
- 📋 **Interface amigável**: Interface web moderna e responsiva
- 📊 **Visualização de resultados**: Mostra códigos originais e ajustados lado a lado
- 📋 **Copiar resultados**: Botão para copiar códigos ajustados para a área de transferência

## Como usar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/LUANFERNANDESRP/code-adjuster-app.git
   cd code-adjuster-app/code_adjuster
   ```

2. **Ative o ambiente virtual**:
   ```bash
   source venv/bin/activate
   ```

3. **Execute o aplicativo**:
   ```bash
   python src/main.py
   ```

4. **Acesse no navegador**:
   Abra http://127.0.0.1:5000 no seu navegador

## Exemplos de uso

### Entrada:
```
1234
A567
B89
12345
C123
456
D7890
```

### Saída:
```
01234
00567
00089
12345
00123
00456
07890
```

## API Endpoints

### POST /api/adjust-codes-text
Ajusta códigos a partir de texto colado.

**Corpo da requisição**:
```json
{
  "text": "1234\nA567\nB89"
}
```

**Resposta**:
```json
{
  "success": true,
  "results": [
    {"original": "1234", "adjusted": "01234"},
    {"original": "A567", "adjusted": "00567"},
    {"original": "B89", "adjusted": "00089"}
  ],
  "total_processed": 3
}
```

### POST /api/adjust-codes
Ajusta uma lista de códigos.

**Corpo da requisição**:
```json
{
  "codes": ["1234", "A567", "B89"]
}
```

## Tecnologias utilizadas

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Banco de dados**: SQLite (opcional)
- **Estilo**: CSS moderno com gradientes e animações

## Estrutura do projeto

```
code_adjuster/
├── src/
│   ├── main.py              # Arquivo principal do Flask
│   ├── routes/
│   │   ├── code_adjuster.py # Rotas para ajuste de códigos
│   │   └── user.py          # Rotas de usuário (template)
│   ├── models/
│   │   └── user.py          # Modelos de banco de dados
│   ├── static/
│   │   ├── index.html       # Interface web
│   │   └── favicon.ico      # Ícone do site
│   └── database/
│       └── app.db           # Banco de dados SQLite
├── venv/                    # Ambiente virtual Python
├── requirements.txt         # Dependências Python
└── README.md               # Este arquivo
```

## Desenvolvimento

Para contribuir com o projeto:

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
