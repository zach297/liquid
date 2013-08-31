function AcousticsCtrl($scope, $http) {
    $http.get('queue', {
        success: function(data) {
            console.log(data);
        }
    });
}