using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class TimeManager : MonoBehaviour
{

    // Inician eventos bajo indicación.
    public static Action OnMinuteChanged;
    public static Action OnHourChanged;

    public static int Minute{get; private set;}
    public static int Hour{get;private set;}

    private float minuteToRealTime = 1f;
    private float timer;

    // Start is called before the first frame update
    void Start()
    {

        // Inicialización de variables.
        Minute = 0;
        Hour = 0;
        timer = minuteToRealTime;
        
    }

    // Update is called once per frame
    void Update()
    {

        timer -= Time.deltaTime; // Identifica el segundo que pasa con cada frame.

        if(timer <= 0)
        {
            Minute++; // Aumenta en 1 segundo.

            OnMinuteChanged?.Invoke(); // Lanza un evento para indicar cambios.

            if(Minute >= 60)
            {
                Hour++; // Aumenta en 1 el valor de los minutos cuando el segundero llega a 60 segundos.
                OnHourChanged?.Invoke(); // Lanza un evento para indicar cambios.
                Minute = 0;
            }

            timer = minuteToRealTime;
        }
        
    }
}
