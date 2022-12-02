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

    public Agent a; 




    // Start is called before the first frame update
    void Start()
    {
        InvokeRepeating("Create", 0.0f, 2f);
    }

    // Update is called once per frame
    void Update()
    {
        a =  gameManager.GetComponent<UrbanMobility>().a; 


        // Debug.Log(a.step_count);
    }

    public void Create()
    {
        numCar = GameObject.FindGameObjectsWithTag("Player").Length;
        int Fcar = a.state_num_cars - numCar;

            if (Fcar >= 1)
            {    
                GameObject car = Instantiate(Carro, new Vector3(0, 0, a.positions[numCar].pos.y), Quaternion.identity);
                car.gameObject.name = "Amogus" + a.positions[numCar].unique_id;
            
                Debug.Log("ID Carro = " + car); 

            }
        
    }
}
