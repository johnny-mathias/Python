import banco
import random
from datetime import datetime

def teste():
    """Teste de funções"""
    
    print("=== TESTE RÁPIDO DAS FUNÇÕES ===\n")
    
    # 1. Teste de recupera_vendas_data
    print("1. Buscando vendas dos últimos 2 anos...")
    data_ini = "01-01-2023"
    data_fim = datetime.now().strftime("%d-%m-%Y")
    vendas = banco.recupera_vendas_data(data_ini, data_fim)
    print(f"   ✅ {len(vendas)} vendas encontradas\n")
    
    # 2. Teste de recupera_vendas_comprador (pegar um comprador aleatório das vendas)
    if vendas:
        comprador_teste = random.choice(vendas)['nm_comprador']
        print(f"2. Buscando vendas do comprador: {comprador_teste}")
        vendas_comprador = banco.recupera_vendas_comprador(comprador_teste)
        print(f"   ✅ {len(vendas_comprador)} vendas encontradas\n")
    
    # 3. Teste de recupera_vendas_vendedor (pegar um vendedor aleatório)
    if vendas:
        vendedor_teste = random.choice(vendas)['nm_vendedor']
        print(f"3. Buscando vendas do vendedor: {vendedor_teste}")
        vendas_vendedor = banco.recupera_vendas_vendedor(vendedor_teste)
        print(f"   ✅ {len(vendas_vendedor)} vendas encontradas\n")
    
    # 4. Teste de altera (atualizar uma venda aleatória do banco)
    alterar_venda = random.choice(vendas)
    print(f"""
4. Alterando venda ID {alterar_venda['id_venda']}
Comprador: {alterar_venda['nm_comprador']}
Produto original: {alterar_venda['ds_produto']}
Valor original: R$ {alterar_venda['vl_total']:.2f}
\n""")

    dados_alteracao = {
        "id_venda": alterar_venda["id_venda"],
        "ds_produto": alterar_venda["ds_produto"] + " (ATUALIZADO)",
        "vl_total": round(alterar_venda["vl_total"] * 1.05, 2),
        "vl_impostos": round(alterar_venda["vl_impostos"] * 1.05, 2)
    }
    banco.altera(dados_alteracao)
    print("   ✅ Venda alterada com sucesso\n")
    
    # 5. Teste de relatório
    print("5. Gerando relatório completo...")
    banco.relatorio_vendas()

if __name__ == "__main__":
    teste()