<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class MainHandler extends Controller
{
    public function getinputURL(){
    	$inputURL = request()->only(['inputURL']);
    	return $inputURL;
    }
}
