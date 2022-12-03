using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;


public class UrbanMobility : MonoBehaviour
{
    public float timeToUpdate = 2.0f;

    private float timer;

    float dt;

    int numCar;

    public static Agent a { get; private set; }
    // Corrutina que hace un get al localhost, guarda el contenido del json en una variable "a" de tipo Agente.
    IEnumerator SendData()
    {
        WWWForm form = new WWWForm();
        form.AddField("bundle", "the data");
        string url = "http://127.0.0.1:5000/step";
        using (UnityWebRequest www = UnityWebRequest.Get(url))
        {
            www.downloadHandler = (DownloadHandler) new DownloadHandlerBuffer();
            www.SetRequestHeader("Content-Type", "application/json");

            yield return www.SendWebRequest(); // Comunicación con python.
            if (www.isNetworkError || www.isHttpError)
            {
                Debug.Log(www.error);
            }
            else
            {
                a = JsonUtility.FromJson<Agent>(www.downloadHandler.text);
            }
        }
    }

    // Start is called before the first frame update
    void Start()
    {
    }

    // Update is called once per frame
    void Update()
    {
        timer -= Time.deltaTime;
        dt = 1.0f - (timer / timeToUpdate);

        if (timer < 0)
        {
#if UNITY_EDITOR
            timer = timeToUpdate; // Resetea el timer.
            StartCoroutine(SendData());
#endif
        }
    }
}
