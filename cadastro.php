<!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta charset="utf-8"/>
	<title></title>
</head>
<body>

<?php 
	// var_dump($_POST);
	// echo "<p> Nome: ".$_POST["nome"]."</P>";
	// echo "<p> Nome: ".$_POST["nome"]."</P>";
	// echo "<p> Nome: ".$_POST["nome"]."</P>";

	// Abrindo conexao
	$conexao = mysqli_connect("127.0.0.1", "root", "", "info3");  
	
	if (!$conexao) {
		echo msqli_connect_errno()."<br/>";
		echo msqli_connect_error()."<br/>";
		
	}

	$resultado = mysqli_query($conexao, "INSERT INTO info3.cadastro (nome, email, senha, nascimento, sexo) values ('".$_POST['nome']."', '".$_POST['email']."', '".$_POST['senha']."', '".$_POST['nascimento']."', '".$_POST['sexo']."');
	

	var_dump($resultado);
?>

</body>
</html>