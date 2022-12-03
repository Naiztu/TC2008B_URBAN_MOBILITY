using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;

public class Spawner : MonoBehaviour
{
    public GameObject gameManager;

    public GameObject Carro;

    public GameObject AltCarro;

    int numCar;

    List<int> carIDs = new List<int>();

    public Agent a;

    void Start()
    {
        InvokeRepeating("Create", 0.0f, 3f); // Invoca a Create cada 3 segundos.
    }

    void Update()
    {
        a = UrbanMobility.a; // Actualiza los datos a los que se encuentran en el servidor.
    }

    /**
        Dentro de la función Create se crean nuevas instancias del GameObject Carro dependiendo
        del número de unique_id que se posean en el modelo del servidor.
        Para evitar que se dupliquen carros con un mismo id, se crea una lista con todos los 
        IDs existentes y se contrastan con aquellos del json.
    **/

    public void Create()
    {
        for (int i = 0; i < a.positions.Count; i++)
        {
            if (!carIDs.Contains(a.positions[i].unique_id))
            {
                carIDs.Add(a.positions[i].unique_id);
                // Para evitar colisiones entre los GameObjects, sus posiciones en "x" cambian.
                GameObject carro =
                    Instantiate(Carro,
                    new Vector3(a.positions[i].pos.x == 0
                            ? -4
                            : a.positions[i].pos.x == 1 ? 0 : 4,
                        0,
                        0),
                    Quaternion.identity);
                carro.GetComponent<Movement>().ID = a.positions[i].unique_id;
            }
        }
    }
}
