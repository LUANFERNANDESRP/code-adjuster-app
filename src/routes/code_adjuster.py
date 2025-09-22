import re
from flask import Blueprint, request, jsonify

code_adjuster_bp = Blueprint('code_adjuster', __name__)

def adjust_code(code_str):
    """
    Ajusta uma string de código para ter 5 dígitos, adicionando zeros à esquerda
    e removendo quaisquer letras. Se não houver números, retorna None.

    Args:
        code_str (str): A string de código a ser ajustada.

    Returns:
        str or None: O código ajustado com 5 dígitos ou None se não houver números.
    """
    # Remove todas as letras da string
    cleaned_code = re.sub(r'[a-zA-Z]', '', str(code_str))

    # Converte para inteiro e formata com 5 dígitos, preenchendo com zeros à esquerda
    # Se a string estiver vazia após a limpeza ou não for numérica, retorna None
    if cleaned_code and cleaned_code.strip():
        try:
            return f'{int(cleaned_code):05d}'
        except ValueError:
            return None
    else:
        return None

@code_adjuster_bp.route('/adjust-codes', methods=['POST'])
def adjust_codes():
    """
    Endpoint para ajustar uma lista de códigos.
    Espera um JSON com uma lista de códigos e retorna os códigos ajustados.
    """
    try:
        data = request.get_json()
        
        if not data or 'codes' not in data:
            return jsonify({'error': 'É necessário fornecer uma lista de códigos'}), 400
        
        codes = data['codes']
        
        if not isinstance(codes, list):
            return jsonify({'error': 'Os códigos devem ser fornecidos como uma lista'}), 400
        
        # Ajusta cada código da lista, filtrando aqueles que não têm números
        adjusted_codes = []
        for code in codes:
            adjusted = adjust_code(code)
            if adjusted is not None:  # Só inclui códigos que têm números
                adjusted_codes.append({
                    'original': code,
                    'adjusted': adjusted
                })
        
        return jsonify({
            'success': True,
            'results': adjusted_codes,
            'total_processed': len(adjusted_codes)
        })
    
    except Exception as e:
        return jsonify({'error': f'Erro interno do servidor: {str(e)}'}), 500

@code_adjuster_bp.route('/adjust-codes-text', methods=['POST'])
def adjust_codes_text():
    """
    Endpoint para ajustar códigos a partir de texto colado.
    Espera um JSON com texto e retorna os códigos ajustados.
    """
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({'error': 'É necessário fornecer o texto com os códigos'}), 400
        
        text = data['text']
        
        # Divide o texto em linhas e remove linhas vazias
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        
        if not lines:
            return jsonify({'error': 'Nenhum código encontrado no texto'}), 400
        
        # Ajusta cada código, filtrando aqueles que não têm números
        adjusted_codes = []
        for line in lines:
            adjusted = adjust_code(line)
            if adjusted is not None:  # Só inclui códigos que têm números
                adjusted_codes.append({
                    'original': line,
                    'adjusted': adjusted
                })
        
        return jsonify({
            'success': True,
            'results': adjusted_codes,
            'total_processed': len(adjusted_codes)
        })
    
    except Exception as e:
        return jsonify({'error': f'Erro interno do servidor: {str(e)}'}), 500
