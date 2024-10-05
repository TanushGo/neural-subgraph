
<code>
pip install torch===1.4.0 -f https://download.pytorch.org/whl/torch_stable.html
pip install --force-reinstall  torch-scatter==2.0.4 torch-sparse==0.6.0 -f https://data.pyg.org/whl/torch-1.4.0+cu101.html
pip install torch-geometric==1.4.3
<code />

## Do not install pytorch by conda it will install multiple versions!!

python3 -m subgraph_matching.alignment --query_path=faces/graph_0.p --target_path=street/multigraph_street.p

python3 -m subgraph_matching.alignment --query_path=faces/graph_2.p --target_path=street/multigraph_street_name_chelsea.p

python -m subgraph_matching.hungarian_algorithm --matrix_path=results/graph_2_alignment.npy  --query_path=faces/graph_2.p --target_path=street/multigraph_street_name_chelsea.p

python -m subgraph_matching.linear_sum --matrix_path=results/graph_2_alignment.npy  --query_path=faces/graph_2.p --target_path=street/multigraph_street_name_chelsea.p