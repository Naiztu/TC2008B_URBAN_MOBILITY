using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Movement : MonoBehaviour
{
    public int speed = 10;

    public int horizontalSpeed = 10;

    public int ID = 0;

    public int posX = 0;

    public int previousX = 0;

    public int posY = 0;

    public int previousY = 0;

    public Vector3 currentPos;

    public Vector3 targetPos;

    public Agent a;

    public void Move()
    {
        // Llama a la información del json obtenida anteriormente por UrbanMobility.
        a = UrbanMobility.a;
        bool flag = false; // Bool auxiliar en la evaluación del estado de los GameObjects.
        for (int i = 0; i < a.positions.Count; i++)
        {
            // si el GameObject posee un ID que se encuentre dentro del json, el bool será verdadero.
            if (a.positions[i].unique_id == ID)
            {

                /**
                    Como el entorno creado se muestra a una escala diferente, las posiciones de "x" y "y"
                    sufren cambios para evitar que los GameObjects colisionen entre ellos. 
                **/
                flag = true;
                posX =
                    a.positions[i].pos.x == 0
                        ? -4
                        : a.positions[i].pos.x == 1 ? 0 : 4;
                posY = (a.positions[i].pos.y * 5);
                break;
            }
        }
        if (a.state_num_cars == 0)
        {
            return;
        }

        if (flag)
        {

            /**
                Si la flag sigue siendo verdadera, se llevará a cabo el movimiento del GameObject 
                a la posición del siguiente step haciendo uso de Lerp.
            **/

            currentPos = transform.position;
            targetPos = new Vector3(posX, 0, posY);
            transform.position = Vector3.Lerp(currentPos, targetPos, Time.deltaTime * 0.7f);
            previousX = posX;
            previousY = posY;
        }
        else
        {
            // En caso contrario, el objeto es destruído al ya no ser parte del ciclo del modelo.
            Destroy(gameObject);
        }
    }

    // Start is called before the first frame update
    void Start()
    {
    }

    // Se llama a la función Move en el update para que los Carros se muevan.
    void Update()
    {
        Move();
    }
}
