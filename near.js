module.exports = {
  NearTime: async function () {
    
    let dateTimeZoneNear = new Date().toLocaleString("en-US", { timeZone: "America/Toronto" });
    let dateTimeZoneLisboa = new Date().toLocaleString("en-US", { timeZone: "Europe/Lisbon" });
    let dateTimeZoneBerlin = new Date().toLocaleString("en-US", { timeZone: "Europe/Berlin" });
    let dateTimeZoneNewYork = new Date().toLocaleString("en-US", { timeZone: "America/New_York" });
    
    let dateNear = FormartStringDate(dateTimeZoneNear, 'Near Time');
    let dateLisboa = FormartStringDate(dateTimeZoneLisboa, 'Lisboa');
    let dateBerlin = FormartStringDate(dateTimeZoneBerlin, 'Berlin');
    let dateNewYork = FormartStringDate(dateTimeZoneNewYork, 'New York');

    let retorno = dateNear.concat(dateLisboa, dateBerlin, dateNewYork);
    return retorno;

  }
};

const FormartStringDate = function(dataString, location) {
      // Data String to Date
      let data = new Date(dataString);

      // Ano
      let year = data.getFullYear();
  
      // Mes
      let month = ("0" + (data.getMonth() + 1)).slice(-2);
  
      // Dia
      let date = ("0" + data.getDate()).slice(-2);
  
      // Hora
      let hours = ("0" + data.getHours()).slice(-2);
  
      // Minutos
      let minutes = ("0" + data.getMinutes()).slice(-2);
  
      // Data Completa
      let formattedDate = date + "/" + month + "/" + year + ",  " + hours + ":" + minutes;
      let retorno = location.concat(' > ', formattedDate, '\n\n');
  return retorno;
}
