#lang racket
;; Exercise 1a
(define (sum-numbers numbers)
  (if(null? numbers)
     0
     (+ (car numbers) (sum-numbers(cdr numbers)))))
;;Exercise 1b
(define (average numbers)
  (cond
    [(null? numbers) 0]
    [else (/ (+ 1 (average (cdr numbers))) sum-numbers (numbers))]))

;;Exercise 2
(define (occurrences numbers n)
      (cond
        [(null? numbers) 0]
        [(= (car numbers) n) (+ 1 (occurrences(cdr numbers) n))]
        [(+ 0 (occurrences(cdr numbers) n))]))

;;Exercise 3
(define (convert numbers)
  (cond
    [(null? numbers) 0]
    [else (+ (car numbers) (* 10 (convert (cdr numbers))))]))
;;Exercise 4
(define (convertFC numbers)
  (cond
    [(empty? numbers) numbers]
    [else (cons (*(- (car numbers) 32) 5/9) (convertFC(cdr numbers)))]))
;;Exercise 5
(define (eliminate-threshold numbers n)
  (cond
    [(null? numbers) empty]
    [(> (car numbers) n) (eliminate-threshold(cdr numbers)n)]
    [(<= (car numbers) n) (cons (car numbers) (eliminate-threshold(cdr numbers) n))]))




(display "Testing eliminate-threshold")
(newline)
(display "Expected: '(1 2 3 4 4 3 2 1), actual: ")
(eliminate-threshold (list 1 2 3 4 5 6 5 4 3 2 1 20) 4)
(display "Expected: '(), actual: ")
(eliminate-threshold (list 1 2 3 4 5 6 5 4 3 2 1 20) 0)
(display "Expected: '(1 2 3 4 5 6 5 4 3 2 1 20), actual: ")
(eliminate-threshold (list 1 2 3 4 5 6 5 4 3 2 1 20) 25)
(newline)