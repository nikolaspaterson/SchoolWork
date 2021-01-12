#lang racket
;;Exercise 4
(define (build-naturals n)
  (build-list n (lambda (x) (* 1 x))))

(define (build-rationals n)
  (build-list n (lambda (x) (/ 1 (+ 1 x)))))

(define (build-evens n)
  (build-list n (lambda (x) (cond
                              [(= x 0) x]
                              [else (* x 2)]))))

;;Exercise 5
(define (cubic a b c)
  (lambda (x) (+ (* x x x) (* a x x) (* b x) c)))

;;Exercise 6
;; a is a procedure and x is the operand.
(define (twice a)
  (lambda (x) (a (a x))))

;;Provided
(define (square x) (* x x))
(define (inc x) (+ x 1))

;;Test
(build-naturals 5)
(build-rationals 5)
(build-evens 5)
((cubic 1 2 3) 4)
((twice square) 5)
((twice inc) 5)