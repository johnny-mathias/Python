INSERT INTO t_vendas (nm_comprador, nm_vendedor, dt_venda, ds_produto, vl_total, vl_impostos) VALUES (
    'Johnny', 
    'Luisa', 
    TO_DATE('10-10-2025', 'DD-MM-YYYY'), 
    'Churros sabor chocolate', 
    2000, 
    300
);

SELECT * FROM t_vendas;