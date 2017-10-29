<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class MainHandler extends Controller
{
    public function getinputURL(){
    	$inputURL = request()->only(['inputURL']);
    	$handle = popen("python victoriaMachineLearning/json_to_dataset.py","r");

    	return $handle;
    }
    public function getinputURL2(){
    	$inputURL = "asdf";
    	$dummy = 
				'{"firstName":"Imran","lastName":"Kazi","bachelorUniv":["University of Pune"],"masterUniv":["Texas State University"],"phdUniv":[],"pastCompany":["BNY Mellon","Texas State University","Allen Technologies"],"pastPosition":["Application Developer","Graduate Research Assistant","Software Engineer"],"currentCompany":"eBay","currentJob":"Software Engineer","bachelorMajor":["Information Technology"],"masterMajor":["Computer Science"],"phdMajor":[],"skills":["Java","JavaScript","jQuery","Spring Framework","RESTful WebServices","SOAP","SQL","C++","C","Python","Oracle","HTML","Linux","Data Structures","PostgreSQL"]}';
			$dummy =
			'
{
	"firstName": "Imran",
	"lastName": "Kazi",
	"bachelorUniv": ["University of Pune"],
	"masterUniv": ["Texas State University"],
	"phdUniv": [],
	"pastCompany": ["BNY Mellon", "Texas State University", 
		"Allen Technologies"],
	"pastPosition": ["Application Developer", 
		"Graduate Research Assistant", "Software Engineer"],
	"currentCompany": "eBay",
	"currentJob": "Software Engineer",
	"bachelorMajor": ["Information Technology"],
	"masterMajor": ["Computer Science"],
	"phdMajor": [],
	"skills":["Java", "JavaScript", "jQuery", 
		"Spring Framework", "RESTful WebServices", "SOAP", "SQL", 
		"C++", "C", "Python", "Oracle", "HTML", "Linux", "Data Structures", "PostgreSQL"]
}';
			$dummydecode = json_decode(json_encode($dummy));
			//print_r($dummydecode);
			//$data = array('a','b','c');
			//print_r($data);
			$dummy2 = escapeshellarg($dummydecode);
    	exec("python3 victoriaMachineLearning/json_to_dataset.py $dummy2",$output);
    	//$result = shell_exec('python3 victoriaMachineLearning/json_to_dataset.py'.escapeshellarg($dummydecode));
    	//var_dump($output);
    	//var_dump($result);
    	//<pre>
    	print("<pre>".print_r($output,true)."</pre>");
    }
}
