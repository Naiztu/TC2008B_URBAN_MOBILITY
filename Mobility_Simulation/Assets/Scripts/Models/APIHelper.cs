using UnityEngine; //Para la clase JsonUtility
using System.Net;
using System.IO;

public static class APIHelper
{
  public static Agent GetNewAgent()
  {
    HttpWebRequest request = (HttpWebRequest) WebRequest.Create("http://127.0.0.1:5000/step");

    HttpWebResponse response = (HttpWebResponse) request.GetResponse();

    StreamReader reader = new StreamReader(response.GetResponseStream());

    string json = reader.ReadToEnd();

    return JsonUtility.FromJson<Agent>(json);
  }
}