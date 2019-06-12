

// let cb=function(data)
// {
//       console.log(data);
//       let dropdown = document.getElementById('country');
//       dropdown.length = 0;
//       let defaultOption = document.createElement('option');
//      defaultOption.text = 'Choose country';
//       dropdown.add(defaultOption);
//       let option;
//            for (let i = 0; i < data.length; i++)
//            {
//                  option = document.createElement('option');
//                  option.text = data[i].name;
//                  option.value = data[i].code;
//                dropdown.add(option);
//             }
// }

     //  let dropdown = document.getElementById('country');
     // //dropdown.length = 0;
     // let defaultOption = document.createElement('option');
     // defaultOption.text = 'Choose country';

     // dropdown.add(defaultOption);
     // dropdown.selectedIndex = 0;

     // let option;
     //      for (let i = 0; i < data.length; i++)
     //       {
     //            option = document.createElement('option');
     //            option.text = data[i].name;
     //            option.value = data[i].code;
     //            dropdown.add(option);
            
       


  


// // For the country
// let dropdown = document.getElementById('country');
// dropdown.length = 0;
// //create the list for the country using createElement
// let defaultOption = document.createElement('option');
// defaultOption.text = 'Choose country';
// //add the one default list country list to dropdown(ul)
// dropdown.add(defaultOption);
// dropdown.selectedIndex = 0;

// const url = 'http://battuta.medunes.net/api/country/all/?key=addecab533626d17217d0867111058f9';

// const request = new XMLHttpRequest();
// request.open('GET', url, true);

// request.onload = function()
// {
//     if (request.status === 200)
//      {
//           const data = JSON.parse(request.responseText);
//           let option;
//           for (let i = 0; i < data.length; i++)
//            {
//                 option = document.createElement('option');
//                 option.text = data[i].name;
//                 option.value = data[i].code;
//                 dropdown.add(option);
//             }
//       } 
//   else {}
// }

// request.onerror = function() 
// {
//  console.error('An error occurred fetching the JSON from ' + url);
// };

// request.send();

