<html>
<head>
	<style type="text/css">
		div.validation { 
		  background-color:#FAAFBE; 
		  width:300px; 
		  height:auto;
			margin-bottom:10px;
		}

		div.validation p { 
		  white-space:normal;
			padding:15px;
			word-wrap:break-word;
		}
		form {
			border:1px solid;
			border-color:black;
			width:350px;
			padding:15px;
		}
		div.even, div.odd {
			width:405px;
			padding:5px;
		}
		div.even {
			background:#E8E8E8;
		}
	</style>
</head>
<div id="Wrapper">
<form action="" method="post">
	Number of nodes: <input type="text" name="nodeCount" /><br/><br/>
	<input type="submit" name="Submit" value="Submit" />
	<input type="submit" name="Reset" value="Reset">
</form>
</html>
<?php
if(!isset($_POST['Reset'])){
	if(isset($_POST['nodeCount'])){
		$count = $_POST['nodeCount'];
		if($count && $count > 0){
			for($i =0;$i<$count;$i++){
				$class = "odd";
				if($i % 2 == 0){$class = "even";}
				echo "<div class='$class'>Node:" . $i . "<br/>initial_token: " . number_format(pow(2,127)*$i/$count,0, '', '') . '</div>';
				//echo "<br/>";
			}
		}
		else{
			echo '
				<div class="validation"> 
				  <p>Number of nodes must be greater than 0.</p>
				</div>
			';
		}
	}
}
?>
</div>