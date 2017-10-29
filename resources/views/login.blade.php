<!DOCTYPE html>
<html lang="en" style="height: 100%;">
    
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{{ $title }}</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
          <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->
        <style>
            .login {
                width: 100wh;
                height: 90vh;
                color: #fff;
                background: linear-gradient(-45deg, #EE7752, #E73C7E, #23A6D5, #23D5AB);
                background-size: 400% 400%;
                -webkit-animation: Gradient 15s ease infinite;
                -moz-animation: Gradient 15s ease infinite;
                animation: Gradient 15s ease infinite;
            }

            @-webkit-keyframes Gradient {
                0% {
                    background-position: 0% 50%
                }
                50% {
                    background-position: 100% 50%
                }
                100% {
                    background-position: 0% 50%
                }
            }

            @-moz-keyframes Gradient {
                0% {
                    background-position: 0% 50%
                }
                50% {
                    background-position: 100% 50%
                }
                100% {
                    background-position: 0% 50%
                }
            }

            @keyframes Gradient {
                0% {
                    background-position: 0% 50%
                }
                50% {
                    background-position: 100% 50%
                }
                100% {
                    background-position: 0% 50%
                }
            }

            .btn-outline-primary{
                border: 1px solid white;
                color: white;
            }
            .btn-outline-primary:hover{
                border: 1px solid #8100C6;
                background-color: #8100C6;
                color: white;
            }
        </style>
    </head>
    <body style="width: 100%; height: 100%;margin: 0;">
        <div class="container" style="margin: 0;  height: 100%;width: 100%;">
            <div class="row" style="height: 100%;">
                <div class='col-lg-8' style="background-color: white; padding: 0; height: 100%;">
                    <img src="img/logo.png" style="max-height: 20em; display: block; margin: 0 auto; margin-top: 20vh;"/>
                </div>
                <div class="col-lg-4 login" style="min-height: 25em; height: 100%;">
                    <div style="margin-top: 30vh;">
                        <h2 style='text-align: center;'>Welcome to Predix,</h2>
                        <h4 style="text-align: center;font-weight:100; font-size: 1em; margin-bottom: 1.5em;">Achieve yer goals ;)</h4>
                        <form style="margin: 0 auto; display: block; width: 60%;">
                              <div class="form-group">
                                <input type="email" class="form-control" id="inputURL" aria-describedby="emailHelp" placeholder="LinkedIn Profile URL">
                              </div>
                              <button type="submit" class="btn btn-outline-primary" style="width: 100%; margin-top:1em;">Lessgo</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>