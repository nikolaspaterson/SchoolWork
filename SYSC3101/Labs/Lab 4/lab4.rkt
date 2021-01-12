#lang racket

;; SYSC 3101 A Winter 2020 Lab 4

;; Exercise 1

(define (make-upcounter counter)
  (lambda ()
    (set! counter (+ counter 1))
    counter))


;; Exercise 2

(define (make-counter counter)

  (define (count-up)
    (set! counter (+ counter 1))
    counter)

  (define (count-down)
    (if (> counter 0)
        (begin (set! counter (- counter 1))
               counter)
        "Counter is 0"))

  (define (dispatch cmd)
    (cond ((eq? cmd 'inc) count-up)
          ((eq? cmd 'dec) count-down)
          (else (error "Unknown command:" cmd))))

  dispatch)


;; Exercise 3

(define (make-counter-with-let initial-count)

  (let ((counter initial-count))

    (define (count-up)
      (set! counter (+ counter 1))
      counter)

    (define (count-down)
      (if (> counter 0)
          (begin (set! counter (- counter 1))
                 counter)
          "Counter is 0"))

    (define (dispatch cmd)
      (cond ((eq? cmd 'inc) count-up)
            ((eq? cmd 'dec) count-down)
            (else (error "Unknown command:" cmd))))

    dispatch))

;; Exercise 4

(define (make-counter-ex4 initial-count)

  (let ((counter initial-count))

    (define (count-up)
      (set! counter (+ counter 1))
      counter)

    (define (count-down)
      (if (> counter 0)
          (begin (set! counter (- counter 1))
                 counter)
          "Counter is 0"))

    (lambda (cmd)
      (cond ((eq? cmd 'inc) count-up)
            ((eq? cmd 'dec) count-down)
            (else (error "Unknown command:" cmd))))))

;;Exercise 5

(define (make-counter-ex5 initial-count)

  (let ((counter initial-count))

    (define (count-up)
      (set! counter (+ counter 1))
      counter)

    (define (count-down)
      (if (> counter 0)
          (begin (set! counter (- counter 1))
                 counter)
          "Counter is 0"))
    (define (get)
      (set! counter (+ counter 0))
      counter)
    
    (define (reset)
      (set! counter 0) counter)

    (lambda (cmd)
      (cond ((eq? cmd 'inc) count-up)
            ((eq? cmd 'dec) count-down)
            ((eq? cmd 'reset) reset)
            ((eq? cmd 'get) get)
            (else (error "Unknown command:" cmd))))))

;;Exercise 6

(define (make-counter-ex6 initial-count inc)

  (let ((counter initial-count))

    (define (count-up)
      (set! counter (+ counter inc))
      counter)

    (define (count-down)
      (if (> counter 0)
          (begin (set! counter (- counter 1))
                 counter)
          "Counter is 0"))
    (define (get)
      (set! counter (+ counter 0))
      counter)
    
    (define (reset)
      (set! counter 0) counter)

    (lambda (cmd)
      (cond ((eq? cmd 'inc) count-up)
            ((eq? cmd 'dec) count-down)
            ((eq? cmd 'reset) reset)
            ((eq? cmd 'get) get)
            (else (error "Unknown command:" cmd))))))

;;Exercise 7

(define (make-counter-ex7 initial-count inc)
  (define max initial-count)
  (set! max initial-count)
  (let ((counter initial-count))

    (define (count-up)
      (cond
        ([> max (+ counter inc)] (set! counter (+ counter inc)))
        ([eq? max (+ counter inc)] (set! counter (+ counter inc)))
        (else (set! max (+ max inc)) (set! counter (+ counter inc))))counter)


    (define (count-down)
      (if (> counter 0)
          (begin (set! counter (- counter 1))
                 counter)
          "Counter is 0"))
    (define (get)
      (set! counter (+ counter 0))
      counter)
    
    (define (reset)
      (set! max 0)
      (set! counter 0) counter)

    (define (maximum)
      (set! max (+ max 0))max)


    (lambda (cmd)
      (cond ((eq? cmd 'inc) count-up)
            ((eq? cmd 'dec) count-down)
            ((eq? cmd 'reset) reset)
            ((eq? cmd 'get) get)
            ((eq? cmd 'max) maximum)
            (else (error "Unknown command:" cmd))))))

(define counter7 (make-counter-ex7 0 2))
((counter7 'inc))
((counter7 'inc))
((counter7 'max))
((counter7 'inc))
((counter7 'max))
((counter7 'dec))
((counter7 'dec))
((counter7 'max))
((counter7 'reset))
((counter7 'max))