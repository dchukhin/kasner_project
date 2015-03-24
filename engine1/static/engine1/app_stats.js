(function(){
    var app = angular.module('statsApp', []);

    app.controller('StatsController', function(){
        this.stats = stuff;
    });

    var stuff = [
        {"browsers":[
            {"name":"firefox"},
            {"name":"chrome"}
            ]
        },
        {"terms":[
            {"name":"google"},
            {"name":"yahoo"}
            ]
        }       
        ]
})();
