using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraMovement : MonoBehaviour
{
    public int Speed = 1;

    void Update()
    {
        // Obtiene el valor de las teclas de dirección al ser pulsadas.
        float xAxisValue = Input.GetAxis("Horizontal") * Speed;
        float zAxisValue = Input.GetAxis("Vertical") * Speed;

        // actualiza la posición de la cámara con los valores obtenidos.
        transform.position = new Vector3(transform.position.x + (-zAxisValue), transform.position.y, transform.position.z + xAxisValue);
    }
}
