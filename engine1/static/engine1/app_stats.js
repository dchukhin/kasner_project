(function(){
    var app = angular.module("statsApp", []);
    console.log('aaa');

    app.controller('StatsController', function(){
        console.log('got here');
        this.browsers = browsers;
        this.terms = terms;
    });

    var browsers = [
        {"name":"firefox"},
        {"name":"chrome"}
    ];

    var terms = [
        {"name":"yahoo"},
        {"name":"google"},
        {"name":"ESPN"}
    ];
/*

        {"browsers":[
            {"name":"firefox"},
            {"name":"chrome"}
            ]
        },
        {"terms":[
            {"name":"google"},
            {"name":"yahoo"},
            {"name":"ESPN"}
            ]
        }       
        ]
*/
})();
