/* global $ */
  $(document).ready(function() {
    'use strict';

    $(window).on('message', function(evt) {
      //Note that messages from all origins are accepted

      //Get data from sent message
      var data = JSON.parse(JSON.stringify(evt.originalEvent.data));
      //Create a new list item based on the data

      //alert(data.gameState.score)
      if (data.messageType == "SAVE"){
        $.ajax({
          url: 'gameShop/play_game/views.py',
          data: {
            'save_message': data
          },
          success: function () {
              alert("A user with this username already exists.");
              var newItem = '\n\t<li>' + (data.score) + '</li>';
              //Add the item to the beginning of the actions list
              $('#actions').prepend(newItem);
          }

        });
      }

      var newItem = '\n\t<li>' + (data.gameState.score) + '</li>';
      //Add the item to the beginning of the actions list
      $('#actions').prepend(newItem);
    });
  });
